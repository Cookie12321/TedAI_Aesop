
import { Inter } from 'next/font/google'
import { useRouter } from 'next/router'

const inter = Inter({ subsets: ['latin'] })

export default function Home() {
  const router = useRouter()

  return (
    <main className="bg-gray-100 h-200 p-8 font-sans">
      
      {/* Header */}
      <header className="text-center text-5xl font-bold text-indigo-600">
        AESOP
      </header>
      
      {/* Themes Container */}
      <div className="mt-16 max-w-lg mx-auto grid gap-4 grid-cols-1 md:grid-cols-1">

        {/* Robot Town */}
        <div className="bg-white p-8 rounded-lg shadow-md flex flex-col">
          <img 
            src="/images/RobotTown1.png"
            className="w-full h-48 object-cover rounded-lg mb-4"
          />
          <h2 className="text-2xl font-bold mb-4">Robot Town</h2>
          <p className="text-gray-700 mb-4">
            A futuristic town where robots live and work.
          </p>
          
          <button 
            className="bg-indigo-500 text-white px-4 py-2 rounded self-start"
            onClick={() => router.push('/themes/robottown')}  
          >
            Explore
          </button>
        </div>

        {/* Animal Jungle */}
        <div className="bg-white p-8 rounded-lg shadow-md flex flex-col">
          <img 
            src="/images/AnimalJungle1.png" 
            className="w-full h-48 object-cover rounded-lg mb-4"
          />
          <h2 className="text-2xl font-bold mb-4">Animal Jungle</h2>
          <p className="text-gray-700 mb-4">
            Lush rainforest teeming with wildlife.
          </p>
        
          <button
            className="bg-indigo-500 text-white px-4 py-2 rounded self-start"
            onClick={() => router.push('/themes/animaljungle')}
          >
            Explore
          </button>
        </div>

      </div>

    </main>
  )
}