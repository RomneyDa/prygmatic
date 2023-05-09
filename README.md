# prygmatic

Open-source python framework for Vercel serverless functions

Opinionated dev stack:

- Poetry package manager
- Wraps pytest for testing

Goals:

- Open-source python framework for Vercel serverless functions
- Wraps around an ASGI-compliant web framework, preferably with the "decorator" approach to api definition. E.g. Sanic
- Support for "tasks" - separate serverless functions or edge functions + scheduling with Vercel CRON jobs
- Simplified support or at least examples for vercel storage (Upstash, blobs, etc.)
- Simple cli/scripts for testing and deployment
- Testing support as a set of network/other utilities that wrap around pytest and/or unittest
- Simple example endpoints/utils for all ^ with accompanying tests
- Async examples

Vercel support a python runtime. [DOCS](https://vercel.com/docs/concepts/functions/serverless-functions/runtimes/python). As of this writing, Vercel supports Python 3.6 and Python 3.9.

Vercel can import git repositories directly. The recommended use of this is:

- clone to your own repository
- [import your respository](https://vercel.com/docs/concepts/deployments/git) into Vercel

To use Vercel serverless, install the Vercel CLI

```bash
npm i -g vercel@latest
```

A simple Vercel serverless Python example is provided [here](https://vercel.com/docs/concepts/functions/serverless-functions/runtimes/python)
