import 'dotenv/config';
import { readdirSync } from 'fs';
import { eleventyImageTransformPlugin } from '@11ty/eleventy-img';
import syntaxHighlight from '@11ty/eleventy-plugin-syntaxhighlight';
import markdownIt from 'markdown-it';
import markdownItAnchor from 'markdown-it-anchor';
import markdownItFootnote from 'markdown-it-footnote';
import { markdownItTable } from 'markdown-it-table';
import { minify } from 'html-minifier-terser';

export const config = {
  dir: {
    input: 'src',
    output: 'dist',
  },
};

const staticDir = `${config.dir.input}/static`;
const bundlesDir = `${config.dir.input}/assets/bundles`;

function getBundleFiles() {
  try {
    const files = readdirSync(bundlesDir);
    const cssFiles = files.filter((file) => file.endsWith('.css'));
    const jsFiles = files.filter((file) => file.endsWith('.js'));

    return {
      css: cssFiles.map((file) => `/${file}`),
      js: jsFiles.map((file) => `/${file}`),
    };
  } catch {
    console.warn('bundles directory not found, webpack may not have run yet');
    return { css: [], js: [] };
  }
}

export default async function (eleventyConfig) {
  eleventyConfig.setUseGitIgnore(false);

  eleventyConfig.addPreprocessor('drafts', '*', (data) => {
    if (data.draft && process.env.ELEVENTY_RUN_MODE === 'build') {
      return false;
    }
  });

  eleventyConfig.setLibrary(
    'md',
    markdownIt({ html: true, typographer: true }),
  );

  const markdownItPlugins = [
    markdownItAnchor,
    markdownItFootnote,
    markdownItTable,
  ];
  markdownItPlugins.forEach((plugin) => {
    eleventyConfig.amendLibrary('md', (mdLib) => mdLib.use(plugin));
  });

  eleventyConfig.addPlugin(eleventyImageTransformPlugin, {
    transformOnRequest: false,
    formats: ['avif', 'webp', 'png'],
    widths: ['auto'],
    htmlOptions: {
      imgAttributes: {
        loading: 'lazy',
        decoding: 'async',
      },
    },
  });

  eleventyConfig.addPlugin(syntaxHighlight, {
    preAttributes: {
      tabindex: 0,
      class: ({ language }) => {
        // https://prismjs.com/plugins/diff-highlight/
        return language.includes('diff')
          ? 'highlight diff-highlight'
          : 'highlight';
      },
    },
  });

  eleventyConfig.addPassthroughCopy({
    [staticDir]: '/',
    // The bundles directory is created by webpack and will be missing when
    // eleventy --serve first runs (in dev). If only the directory name is
    // specified here, eleventy won't copy files inside it to dist when they
    // appear. Using a glob pattern ensures the files are copied.
    [`${bundlesDir}/**`]: '/',
  });

  eleventyConfig.addPassthroughCopy(`${config.dir.input}/posts`, {
    // https://github.com/timkendrick/recursive-copy/blob/4c9a8b8a4bf573285e9c4a649a30a2b59ccf441c/README.md#usage
    debug: true,
    filter: '**/*.{mp4,cast}',
    // copies src/posts/post-name/foo.mp4 to dist/post-name/foo.mp4
    rename: (filePath) => `../${filePath}`,
  });

  eleventyConfig.addShortcode('cssPath', () => {
    const bundles = getBundleFiles();
    const mainFile = bundles.css.find((file) => file.includes('main'));
    return mainFile || '';
  });

  eleventyConfig.addShortcode('cssPathVendor', () => {
    const bundles = getBundleFiles();
    const vendorFile = bundles.css.find((file) => file.includes('vendor'));
    return vendorFile || '';
  });

  eleventyConfig.addShortcode('jsPath', () => {
    const bundles = getBundleFiles();
    const mainFile = bundles.js.find((file) => file.includes('main'));
    return mainFile || '';
  });

  eleventyConfig.addShortcode('jsPathVendor', () => {
    const bundles = getBundleFiles();
    const vendorFile = bundles.js.find((file) => file.includes('vendor'));
    return vendorFile || '';
  });

  eleventyConfig.addShortcode('asciinema', function (castFile) {
    const castID = castFile.split('.').join('-');
    const options = {
      cols: 80,
      rows: 10,
      preload: true,
      autoPlay: true,
      loop: true,
      theme: 'monokai',
    };

    return `<div id="${castID}"></div>
<script>
document.addEventListener("DOMContentLoaded", function() {
  window.AsciinemaPlayer.create("${castFile}", document.getElementById("${castID}"), ${JSON.stringify(options)});
});
</script>`;
  });

  eleventyConfig.addTransform(
    'minifyMarkup',
    async function (content, outputPath) {
      if (outputPath) {
        if (outputPath.endsWith('.html')) {
          try {
            // https://github.com/terser/html-minifier-terser/blob/c4a7ae0bd08b1a438d9ca12a229b4cbe93fc016a/README.md#options-quick-reference
            return await minify(content, {
              collapseWhitespace: true,
              minifyCSS: true,
              minifyJS: true,
              quoteCharacter: '"',
              removeAttributeQuotes: true,
              removeComments: true,
              removeEmptyAttributes: true,
              removeOptionalTags: true,
              removeRedundantAttributes: true,
              removeScriptTypeAttributes: true,
              removeStyleLinkTypeAttributes: true,
              sortAttributes: true,
              sortClassName: true,
              useShortDoctype: true,
            });
          } catch (err) {
            console.error('failed to minify html', err);
            return content;
          }
        }

        if (outputPath.endsWith('.xml')) {
          try {
            return await minify(content, {
              caseSensitive: true,
              collapseWhitespace: true,
              conservativeCollapse: true,
              html5: false,
              keepClosingSlash: true,
              quoteCharacter: '"',
              removeComments: true,
            });
          } catch (err) {
            console.error('failed to minify xml', err);
            return content;
          }
        }
      }

      return content;
    },
  );
}
