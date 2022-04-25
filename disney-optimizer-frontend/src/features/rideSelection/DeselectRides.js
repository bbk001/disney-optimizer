import React, { useState } from 'react';
import { getRideInfo } from '../../utils/funcs';

function DeselectRides({setReadyToSort}) {
  const [excludedRides, setExcludedRides] = useState(JSON.parse(localStorage.getItem('excluded-rides')) || []);
  const rideInfo = getRideInfo();
  console.log(excludedRides)

  return (
    <div className='page'>
      <div className='explainer'>First select any rides you are not interested in even if the line is short.</div>
      <table>
        <tbody>
          {Object.keys(rideInfo).map(ride => 
            excludedRides.includes(ride) ? null :
              <tr key={ride}>
                <td>{rideInfo[ride].rideName}</td>
                <td>
                  <button 
                    onClick={() => setExcludedRides([...excludedRides, ride])}
                  >Remove</button>
                </td>
              </tr>
          )}
        </tbody>
      </table>
      <button
        onClick={()=> {
          localStorage.setItem('excluded-rides', JSON.stringify(excludedRides))
          setReadyToSort(true)
        }}
      >Continue</button>
      <button onClick={()=> {
        localStorage.removeItem('excluded-rides')
        setExcludedRides([])
      }}>
        Reset Selections
      </button>
    </div>
  )
}

export default DeselectRides