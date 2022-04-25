import React, { useState } from 'react';
import { getRideInfo } from '../../utils/funcs';

function DeselectRides({setReadyToRank}) {
  const [rideInfo, setRideInfo] = useState(getRideInfo());

  return (
    <div>
      <div>First select any rides you are not interested in even if the line is short.</div>
      <table>
        <tbody>
          {Object.keys(rideInfo).map(ride => 
            <tr key={ride}>
              <td>{rideInfo[ride].rideName}</td>
              <td>
                <button 
                  onClick={() => {
                    let excludedRides = JSON.parse(localStorage.getItem('excluded-rides')) || []
                    excludedRides.push(ride)
                    localStorage.setItem('excluded-rides', JSON.stringify(excludedRides))
                    setRideInfo(getRideInfo())
                  }}
                >Remove</button>
              </td>
            </tr>
          )}
        </tbody>
      </table>
      <button
        onClick={()=>{
          localStorage.setItem('ready-to-rank', true)
          setReadyToRank(true)
        }}
      >Continue</button>
      <button onClick={()=>localStorage.setItem('excluded-rides', JSON.stringify([]))}>
        Reset Selections
      </button>
    </div>
  )
}

export default DeselectRides