export default {
  layout: 'post.liquid',
  tags: ['post'],
  eleventyComputed: {
    permalink: (data) =>
      data.page.filePathStem.replace('/posts/', '/') + '.html',
  },
};
