import { Routes, Route, HashRouter } from 'react-router-dom'

import Login from '../Paginas/login';

export default function Navegador(){
    return (
        <HashRouter>
            <Routes>
                <Route path="/" element ={<Login/>}/> {/*home*/}
                <Route path="/Login" element ={<Login/>}/> 
                {/*<Route path="/Login/:disk/:part" element ={<Login newIp={ip}/>}/>*/}
            </Routes>
        </HashRouter>
    );
}