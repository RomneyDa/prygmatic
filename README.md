# prygmatic

Open-source python framework for Vercel serverless functions

Opinionated dev stack:

- Poetry package manager
- Wraps pytest for testing

Goals:

- Builds api from simple decorators
- Creates separate serverless functions - "tasks" - that can be triggered asyncronously
- Vercel edge functions support
- Vercel storage support! Upstash, blobs, etc.
- Threading functionality
- Async functionality using trio or asyncio
- Support for Vercel cron jobs - preferably with a simple decorator - uses that for the idea of scheduled tasks as well

Vercel support a python runtime. [DOCS](https://vercel.com/docs/concepts/functions/serverless-functions/runtimes/python). As of this writing, Vercel supports Python 3.6 and Python 3.9.

Vercel can import git repositories directly. The recommended use of this is:

- clone to your own repository
- [import your respository](https://vercel.com/docs/concepts/deployments/git) into Vercel

To use Vercel serverless, install the Vercel CLI

```bash
npm i -g vercel@latest
```

A simple Vercel serverless Python example is provided [here](https://vercel.com/docs/concepts/functions/serverless-functions/runtimes/python)
