import React, { useState } from 'react';

function Plan(props) {
  return (
    <table>
      <thead>
        <tr>
          <th>Ride</th>
          <th>Time</th>
        </tr>
      </thead>
      <tbody>
        {props.plans.map(ridePlan => 
          <tr>
            <td>{ridePlan.rideName}</td>
            <td>{ridePlan.startTime}</td>
          </tr>
        )}
      </tbody>
    </table>
  );
}

export default Plan;
