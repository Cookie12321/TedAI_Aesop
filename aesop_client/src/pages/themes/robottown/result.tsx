import { useRouter } from 'next/router';

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
    <div>
    <div>RESPONSE</div>

    <div>{response_data.generated_story}</div>
    </div>
    )
  }
  export default ResultPage;