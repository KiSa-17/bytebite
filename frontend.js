import React, { useState, useEffect, useRef } from 'react';
import { Button } from "@/components/ui/button"; 
import { Card, CardContent } from "@/components/ui/card";

const medications = [
  { id: 1, name: 'Aspirin', time: '10:00 AM' },
  { id: 2, name: 'Vitamin D', time: '2:00 PM' }
];

export default function MedicationReminder() {
  const [currentMed, setCurrentMed] = useState(null);
  const [waitingForResponse, setWaitingForResponse] = useState(false);
  const [escalated, setEscalated] = useState(false);
  const waitingRef = useRef(false);

  useEffect(() => {
    const interval = setInterval(() => {
      checkMedications();
    }, 60000); 

    checkMedications();

    return () => clearInterval(interval);
  }, []);

  const checkMedications = () => {
    const now = new Date();
    const currentHour = now.getHours();
    const currentMinute = now.getMinutes();

    medications.forEach((med) => {
      const [time, modifier] = med.time.split(' ');
      let [medHour, medMinute] = time.split(':').map(Number);

      if (modifier === 'PM' && medHour !== 12) {
        medHour += 12;
      } else if (modifier === 'AM' && medHour === 12) {
        medHour = 0;
      }

      if (currentHour === medHour && Math.abs(currentMinute - medMinute) <= 1) {
        if (!waitingRef.current) {
          sendVoiceReminder(med);
        }
      }
    });
  };

  const sendVoiceReminder = (med) => {
    setCurrentMed(med);
    setWaitingForResponse(true);
    setEscalated(false);
    waitingRef.current = true;

    const msg = new SpeechSynthesisUtterance(Time to take your medication: ${med.name});
    window.speechSynthesis.speak(msg);

    setTimeout(() => {
      if (waitingRef.current) {
        escalateToFamily(med);
      }
    }, 60000); 
  };

  const handleResponse = (response) => {
    setWaitingForResponse(false);
    waitingRef.current = false;

    if (response === 'taken') {
      alert('Great! Medication confirmed.');
    } else {
      alert('Okay, we will remind you again soon.');
      setTimeout(() => {
        if (!waitingRef.current) {
          sendVoiceReminder(currentMed);
        }
      }, 300000); 
    }
  };

  const escalateToFamily = (med) => {
    setEscalated(true);
    waitingRef.current = false;
    alert(Alert sent to family: Patient missed ${med.name});
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen p-4">
      <Card className="w-full max-w-md shadow-lg">
        <CardContent className="flex flex-col gap-4">
          <h1 className="text-2xl font-bold text-center">Medication Reminder</h1>
          {currentMed ? (
            <div className="text-center">
              <p className="text-lg">Please take your <b>{currentMed.name}</b>.</p>
              <div className="flex gap-4 mt-4 justify-center">
                <Button onClick={() => handleResponse('taken')}>I took it</Button>
                <Button variant="outline" onClick={() => handleResponse('later')}>Remind me later</Button>
              </div>
              {escalated && (
                <p className="text-red-500 mt-4">Escalation: Family has been notified!</p>
              )}
            </div>
          ) : (
            <p className="text-center">No reminders right now.</p>
          )}
        </CardContent>
      </Card>
    </div>
  );
}
