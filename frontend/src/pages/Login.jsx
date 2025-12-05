import React from 'react'
import Forms from '../components/Forms.jsx'

const Login = () => {
  return (
    <div>
      <Forms route={"/api/token/"} method={"login"} />
    </div>
  )
}

export default Login