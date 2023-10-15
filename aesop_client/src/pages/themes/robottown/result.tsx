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
    </div>
    )
  }
  export default ResultPage;