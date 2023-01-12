function Reformat(metadata, value, front_string, end_string, unknown_value) {
    if (metadata[value]) {
        return front_string + metadata[value] + end_string
    }
    else {
        return unknown_value
    }
}

return Reformat(dv.current(), input.value, input.front_string, input.end_string, input.unknown_value)