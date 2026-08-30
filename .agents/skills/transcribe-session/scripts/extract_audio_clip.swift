#!/usr/bin/env swift

import AVFoundation
import CoreMedia
import Foundation

func fail(_ message: String, code: Int32 = 2) -> Never {
    FileHandle.standardError.write(Data(("error: \(message)\n").utf8))
    exit(code)
}

func describe(_ error: Error?) -> String {
    guard let error else {
        return "no diagnostic was provided"
    }
    let nsError = error as NSError
    var parts = [
        "\(nsError.domain) code \(nsError.code): \(nsError.localizedDescription)"
    ]
    if let reason = nsError.localizedFailureReason {
        parts.append(reason)
    }
    if let underlying = nsError.userInfo[NSUnderlyingErrorKey] as? NSError {
        parts.append(
            "underlying \(underlying.domain) code \(underlying.code): "
                + underlying.localizedDescription
        )
    }
    return parts.joined(separator: "; ")
}

guard CommandLine.arguments.count == 5 else {
    fail("usage: extract_audio_clip SOURCE OUTPUT START_SECONDS DURATION_SECONDS")
}

let sourcePath = CommandLine.arguments[1]
let outputPath = CommandLine.arguments[2]
guard let startSeconds = Double(CommandLine.arguments[3]),
      let durationSeconds = Double(CommandLine.arguments[4]),
      startSeconds >= 0,
      durationSeconds > 0 else {
    fail("start and duration must be valid positive times")
}

let sourceURL = URL(fileURLWithPath: sourcePath)
let outputURL = URL(fileURLWithPath: outputPath)
let asset = AVURLAsset(url: sourceURL)
let tracks: [AVAssetTrack]
do {
    tracks = try await asset.loadTracks(withMediaType: .audio)
} catch {
    fail("could not load source audio tracks: \(describe(error))")
}
guard let track = tracks.first else {
    fail("source contains no audio track")
}
let formatDescriptions: [CMFormatDescription]
do {
    formatDescriptions = try await track.load(.formatDescriptions)
} catch {
    fail("could not load the source audio format: \(describe(error))")
}
guard let audioFormatDescription = formatDescriptions.first else {
    fail("source audio track has no format description")
}

let reader: AVAssetReader
do {
    reader = try AVAssetReader(asset: asset)
} catch {
    fail("could not create AVAssetReader: \(describe(error))")
}
let trackOutput = AVAssetReaderTrackOutput(track: track, outputSettings: nil)
trackOutput.alwaysCopiesSampleData = false
guard reader.canAdd(trackOutput) else {
    fail("AVFoundation cannot read the source audio track")
}
reader.add(trackOutput)
reader.timeRange = CMTimeRange(
    start: CMTime(seconds: startSeconds, preferredTimescale: 600),
    duration: CMTime(seconds: durationSeconds, preferredTimescale: 600)
)

let writer: AVAssetWriter
do {
    writer = try AVAssetWriter(outputURL: outputURL, fileType: .m4a)
} catch {
    fail("could not create AVAssetWriter: \(describe(error))")
}
let writerInput = AVAssetWriterInput(
    mediaType: .audio,
    outputSettings: nil,
    sourceFormatHint: audioFormatDescription
)
writerInput.expectsMediaDataInRealTime = false
guard writer.canAdd(writerInput) else {
    fail("AVFoundation cannot write the source audio format to M4A")
}
writer.add(writerInput)

guard reader.startReading() else {
    fail("AVFoundation could not start reading: \(describe(reader.error))")
}
guard writer.startWriting() else {
    fail("AVFoundation could not start writing: \(describe(writer.error))")
}
guard let firstBuffer = trackOutput.copyNextSampleBuffer() else {
    fail("AVFoundation returned no audio samples for the requested range")
}
writer.startSession(
    atSourceTime: CMSampleBufferGetPresentationTimeStamp(firstBuffer)
)

var appendedBuffers = 0
var nextBuffer: CMSampleBuffer? = firstBuffer
while let sampleBuffer = nextBuffer {
    while !writerInput.isReadyForMoreMediaData {
        if writer.status == .failed || writer.status == .cancelled {
            fail("AVFoundation audio writing failed: \(describe(writer.error))")
        }
        usleep(1_000)
    }
    guard writerInput.append(sampleBuffer) else {
        fail("AVFoundation rejected an audio sample: \(describe(writer.error))")
    }
    appendedBuffers += 1
    nextBuffer = trackOutput.copyNextSampleBuffer()
}

guard reader.status == .completed else {
    fail("AVFoundation audio reading failed: \(describe(reader.error))")
}
guard appendedBuffers > 0 else {
    fail("AVFoundation returned no audio samples for the requested range")
}
writerInput.markAsFinished()
await writer.finishWriting()
guard writer.status == .completed else {
    fail("AVFoundation could not finish the M4A clip: \(describe(writer.error))")
}
