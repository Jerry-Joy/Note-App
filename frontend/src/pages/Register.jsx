import React from 'react'
import Forms from '../components/Forms.jsx' 

const Register = () => {
  return (
    <div>
      <Forms route={"/api/user/register/"} method={"register"}/>
    </div>
  )
}

export default Register