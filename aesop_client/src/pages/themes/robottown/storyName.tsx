"use client"

import { useRouter } from 'next/router';
import { useState } from 'react';

interface Story {
    conflict_name: string;
    prompts: string[];
    description: string;
}

interface Response {
    prompt: string;
    response: string;
}

interface FormValues {
    responses: Response [];
    conflict_name: string;
}

export default function StoryPageForm() {
    // Get router
    const router = useRouter();

      // Get query param and cast to Story type
    const { story } = router.query as { story: string };
    const storyData = JSON.parse(story) as Story;

    const [isSubmitting, setIsSubmitting] = useState<boolean>(false);

    const [formValues, setFormValues] = useState<FormValues>({
        responses: [],
        conflict_name: storyData.conflict_name
    });

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        console.log(formValues);
        setIsSubmitting(true);
        
        try {
          const response = await fetch('http://localhost:8080/api/submit_exercise', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify(formValues)
          });
    
          if(!response.ok) {
            throw new Error(response.statusText);
          }
          const data = await response.json();
          console.log(data);
          router.push({
            pathname: '/themes/robottown/result',
            query: { data: JSON.stringify(data) }
          });

          alert('Form submitted!');
          
        } catch(error) {
          alert('Error submitting form');
        }
        
        setIsSubmitting(false);
      };


  return (
    <form className="space-y-4" onSubmit={handleSubmit}>
    <div className="bg-gray-100 min-h-screen p-8">
        
      {/* Center contents */}
      <div className="max-w-lg mx-auto">

        {/* Add padding and background */}
        <div className="bg-white p-8 rounded-lg shadow-md">
        
          {/* Styled header */}
          <h1 className="text-3xl font-bold text-indigo-600 mb-4">
            User Input Exercise
          </h1>

          {/* Map through prompts */}
          {storyData.prompts.map((prompt, index) => (

            // Card for each prompt 
            <div key={prompt} className="mb-4">

              {/* Styled prompt header */}
              <h2 className="text-xl font-semibold border-b pb-2">
                {prompt}
              </h2>
              {/* Styled input */}
              <input 
                value={formValues.responses[index]?.response}
                onChange={e => {
                    const newResponses = [...formValues.responses];
                    newResponses[index] = {
                      prompt,
                      response: e.target.value
                    };
                    setFormValues({...formValues, responses: newResponses});
                  }}
                className="w-full border mt-2 rounded px-3 py-2 text-gray-700 focus:outline-none focus:shadow-outline"
              />

            </div>
          ))}
        
        </div>

      </div>
      <div className="p-4 flex flex-col space-y-4">
            <button 
                className="bg-blue-500 text-white rounded p-2"
                type="submit"
                disabled={isSubmitting}
            >
                {isSubmitting ? 'Submitting...' : 'Submit'}
            </button>
        </div>
    </div>

    </form>
  );
}

