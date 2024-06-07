Generate some markdown:

```ts
import { tsMarkdown } from 'ts-markdown';

// Make markdown entries
const entries = [
  {
    h4: 'Hello, world!',
  },
  {
    blockquote: "Let's generate markdown!",
  },
  { p: 'Generating markdown from data can be simple. All you need are:' },
  {
    ol: [
      'objects',
      'a function',
      {
        text: ['and a place to run ', { emoji: 'checkered_flag' }],
      },
    ],
  },
];

return tsMarkdown(entries); // returns the markdown document as a string
```

