# prygmatic

Open-source python framework for Vercel serverless functions

Vercel support a python runtime. [DOCS](https://vercel.com/docs/concepts/functions/serverless-functions/runtimes/python). As of this writing, Vercel supports Python 3.6 and Python 3.9.

Vercel can import git repositories directly. The recommended use of this is:

- clone to your own repository
- [import your respository](https://vercel.com/docs/concepts/deployments/git) into Vercel

To use Vercel serverless, install the Vercel CLI

```bash
npm i -g vercel@latest
```

A simple Vercel serverless Python example is provided [here](https://vercel.com/docs/concepts/functions/serverless-functions/runtimes/python)
