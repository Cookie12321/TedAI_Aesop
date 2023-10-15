
import { GetServerSideProps } from 'next'
import { useRouter } from 'next/router';
import { useState } from 'react';

interface Story {
  conflict_name: string;
  prompts: string[];
  description: string;
}

interface Props {
  stories: Story[];
}

// const [answers, setAnswers] = useState<string[]>([])
// const [currentPrompt, setCurrentPrompt] = useState<string|null>(null)

export default function RobotTown({ stories }: Props) {
    
    const router = useRouter()
    const handleClick = (story: Story) => {
        router.push({
            pathname: '/themes/robottown/storyName',
            query: { story: JSON.stringify(story) }
          }, `/themes/robottown/${story.conflict_name}`)
    }
  return (
    <div className="p-4 grid place-content-center h-screen">
      <h1 className="p-4 mt-10 text-3xl font-bold">Robot Town</h1>
      <img 
        src="https://cdn.stability.ai/assets/org-DoLDPy7xs659iq1YsM82XpcE/00000000-0000-0000-0000-000000000000/f70eb5f1-073f-cc2e-b449-405636d65699" 
        alt="Header"
        className="aspect-video w-full max-h-96 object-cover" 
      />
      <p className='grid place-content-center'>
      Nestled deep in the mountains lies a secret town where robots live and work. Every morning as the sun peeks over the peaks, the robots whir to life and start their daily routines around the metal metropolis.
      </p>
        <div className="p-4 flex flex-col space-y-4">
        {stories.map(story => (
            <button 
                className="bg-blue-500 text-white rounded p-2"
                key={story.conflict_name}
                onClick={() => handleClick(story)}
            >
                {story.conflict_name} 
            </button>
            ))}
        </div>
        <div>
           
        </div>

    
    </div>
  )
} 

export const getServerSideProps: GetServerSideProps<Props> = async () => {
  
//   const res = await fetch('https://api.example.com/robots')
//   const stories = await res.json()
  const stories = [
    {
      conflict_name: "The Disappearing Robot Parts",
      prompts: ["What starts happening in Robot Town that makes the robots realize some of their essential robot parts are disappearing?",
        "How do the robots feel when they discover that their parts are missing?",
        "What do the robots do to try to find their missing parts?",
        "What do the robots do when they find out who is taking their parts?",
        "How do the robots ultimately recover their missing parts, and what do they learn from this experience?"],
      description: "One day, different parts in Robot Town go missing. What happens next?"
    },
    {
      conflict_name: "The Broken Bridge",
      prompts: ["What happens to the bridge in Robot Town that connects two important parts of the town, making it impossible for the robots to get from one side to the other?", 
        "How do the robots react when they realize they can't cross the bridge?",
        "What do the robots do to try to fix the bridge?",
        "What do the robots do when they find out who broke the bridge?",
        "How do the robots ultimately fix the bridge, and what do they learn from this experience?"],
      description: "One day, the bridge in Robot Town breaks. What happens next?"
    },
    {
        conflict_name: "The Robot Town Games Competition",
        prompts: ["What is the competition known as the Robot Town Games about?", 
        "What happens when the robots compete in the Robot Town Games?",
        "What do the robots do to prepare for the Robot Town Games?",
        "What do the robots do when they find out who is cheating in the Robot Town Games?",
        "How do the robots ultimately win the Robot Town Games, and what do they learn from this experience?"],
        description: "One day, the robots in Robot Town decide to have a competition. What happens next?"
    }
  ]

  return {
    props: {
      stories
    }
  }
}