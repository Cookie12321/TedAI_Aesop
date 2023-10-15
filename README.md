# Aesop.ai: Educational Choose-Your-Own-Adventure AI Storytelling with Psychological Analysis

Aesop.ai uses OpenAI to create a transformative educational experience with narrative storytelling and psychological analysis. Aesop prompts the user to create context regarding a story's setting, and then writes out a story based on the user's responses to the prompts. Also, Aesop utilizes the Social Cognition and Object Relations Scale-Global Rating Method (SCORS-G) as a rubric to measure the user's mental headspace based on their answers to the story-telling prompts.

Students will be flexing their literary caps and critical thinking skills when filling out prompts. Educators and parents will have potential early warnings signs of declining mental health amongs Aesop users from the AI analysis of the user prompt responses.

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
npm install next@latest react@latest react-dom@latest
npm install react-pageflip
npm install recharts
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

We use Flask, React, SQLite3, Docker, OpenAI API, and DALL E 3.

## Thank you

Many thanks to Kungbib because this is a fork off of their https://github.com/Kungbib/flask-docker-example, which we used to help jumpstart our Flask web app on Docker.
