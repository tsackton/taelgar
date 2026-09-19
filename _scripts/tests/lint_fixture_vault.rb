# frozen_string_literal: true

require "fileutils"
require "json"
require_relative "../generate_taelgar_lint_values"

# Only test-owned declarations are copied. Never seed this from the working vault
# or its generated sidecar: editing/deleting real notes must not affect tests.
module LintFixtureVault
  def self.write_catalog(root)
    fixture_root = File.join(__dir__, "fixtures", "lint-governance")
    FileUtils.cp_r(File.join(fixture_root, "_MoC"), root)
    output = File.join(root, TaelgarLintValues::OUTPUT_PATH)
    FileUtils.mkdir_p(File.dirname(output))
    File.write(output, "#{JSON.pretty_generate(TaelgarLintValues.build(root))}\n")
  end
end
