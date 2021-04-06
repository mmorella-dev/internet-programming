const syntaxHighlight = require("@11ty/eleventy-plugin-syntaxhighlight");

module.exports = function(eleventyConfig) {
  eleventyConfig.addPlugin(syntaxHighlight);
  eleventyConfig.setTemplateFormats([
    "md",
    "liquid",
    "css", // css is not yet a recognized template extension in Eleventy
    "jpg", "png"
  ]);
  eleventyConfig.addPassthroughCopy("static");
};