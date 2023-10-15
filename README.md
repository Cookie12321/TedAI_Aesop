# Educational Choose-Your-Own-Adventure AI Storytelling with Psychological Analysis

Our project for the TedAI Hackathon uses OpenAI to create a transformative educational experience with narrative storytelling and psychological analysis. We utilize the Social Cognition and Object Relations Scale-Global Rating Method (SCORS-G) as a rubric to measure the user's mental headspace based on their answers to the story-telling prompts.

Learn more about SCORS-G at https://www.scors-g.com/.

## Team Aesop

Tony (Baek) Choi - Software Engineer

Albert Le - Data Engineer

## Installation

```bash
git clone https://github.com/Cookie12321/TedAI_Aesop
cd TedAI_Aesop
```

## Run

The following will build and deploy the Flask backend container locally.

```bash
docker-compose build
docker-compose up
```

Go to http://localhost:8080/ to view the backend.

Then go into the React client folder.

```bash
cd aesop_client/
```

One of the following commands will start the React frontend component locally.

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Go to http://localhost:3000 to view the frontend.

## Tech Stack

We use Flask, React, Docker, and the OpenAI API.

## Thanks

Many thanks to Kungbib because this is a fork off of https://github.com/Kungbib/flask-docker-example, which we used to help jumpstart our Flask web app on Docker.
