# SocialBot AI

A separate SaaS platform for creating, scheduling, and publishing AI-generated short-form videos to Facebook and Instagram.

## Product scope
- Public user registration and sign-in
- Workspace dashboard
- AI-assisted reel scripts, scene planning, captions, and subtitles
- 9:16 video rendering pipeline
- Connect Facebook Pages and Instagram Professional accounts through official Meta OAuth
- Publish now or schedule posts
- Publishing history and analytics

## Architecture (initial)
- `frontend/`: Next.js web application
- `backend/`: Python FastAPI API
- PostgreSQL: users, connected accounts, jobs, and publishing history
- Redis + worker: background rendering and scheduled publishing
- FFmpeg: video assembly
- Gemini: script and content assistance
- Object storage: generated media

## Safety and integration notes
- Meta publishing will use official Meta APIs and user-authorized OAuth only.
- Facebook/Instagram permissions, App Review, and business verification may be required before public users can publish.
- Instagram publishing requires an eligible Professional account.
- Never commit API keys, OAuth secrets, access tokens, or database passwords. Use environment variables.

## Development status
Initial repository scaffold. No connection to or changes in the separate News Bot project.
