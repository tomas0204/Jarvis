import "./layout/Dashboard.tsx" 
import Dashboard from "./layout/Dashboard.tsx"
import { jarvisService } from "./services/jarvis.ts"
import { useEffect } from "react"

function App() {
    useEffect(() => {
        jarvisService
            .sendMessage('abre chrome')
            .then(result => {
            console.log('RESPUESTA DE JARVIS:', result)
            })
            .catch(error => {
            console.error(error)
            })
        }, [])
    return (
    <Dashboard />
)
}

export default App