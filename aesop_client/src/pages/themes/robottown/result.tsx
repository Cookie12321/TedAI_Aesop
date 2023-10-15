import { useRouter } from 'next/router';
import HTMLFlipBook from 'react-pageflip';

interface api_response {
  generated_story: string[];
  SEL_scoring: string;
}


const ResultPage = () => {
  const router = useRouter();
  const { data } = router.query as { data: string };
  console.log(data);
  const response_data = JSON.parse(data) as api_response;

  async function handleOnClick() {
    const response = await fetch('http://localhost:8080/api/get_scores');
    const json = await response.json();
    console.log(json);
    router.push({
      pathname: '/themes/robottown/dataVis',
      query: { data: JSON.stringify(json) }
    });
  }

  console.log(response_data);
    // Get API response from query
  
    return (
    <div className='flex items-center justify-center h-screen bg-gray-200'>
      <div className="max-w-lg w-full">
      <HTMLFlipBook width={400} height={500}>
        {response_data.generated_story.map((pagecontent, index) => (
          <div className="demoPage p-4 bg-white shadow-lg">
            <h2 className="page-number text-xl font-bold mb-4">
              Page {index + 1}
            </h2>
              <div className="h-full flex flex-col justify-center">
                <p className='text-gray-800 max-w-prose mx-auto'>
                  {pagecontent}
                </p>
              </div>
            </div>
        ))
        }
        
      </HTMLFlipBook>
      </div>
      <button className='bg-indigo-500 text-white absolute bottom-4 right-4 p-4 rounded self-start'
              onClick={handleOnClick}>
        Data Visualization
      </button>
    </div>
    )
  }
  export default ResultPage;