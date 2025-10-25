import { defineConfig, globalIgnores } from 'eslint/config';
import globals from 'globals';
import js from '@eslint/js';
import { includeIgnoreFile } from '@eslint/compat';
import { fileURLToPath } from 'node:url';

const gitignorePath = fileURLToPath(new URL('.gitignore', import.meta.url));

export default defineConfig([
  includeIgnoreFile(gitignorePath, 'imported .gitignore patterns'),
  globalIgnores(['**/*.min.js']),
  {
    files: ['**/*.js'],
    ignores: ['src/assets/js/**/*.js'],
    languageOptions: { globals: globals.node },
  },
  {
    files: ['src/assets/js/**/*.js'],
    languageOptions: { globals: globals.browser },
  },
  { files: ['**/*.js'], plugins: { js }, extends: ['js/recommended'] },
]);
