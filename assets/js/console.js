function greeting() {
  const emoji = Date.now() % 2 ? '👀' : '👋';
  console.info(emoji);
}

greeting();
