// twix-ai-frontend/src/components/BackendMessage.tsx
import React, { useState, useEffect } from 'react';
import axios from 'axios';

const BackendMessage: React.FC = () => {
    const [message, setMessage] = useState<string>('');

    useEffect(() => {
        axios.get('http://localhost:5000/')
            .then(response => {
                setMessage(response.data);
            })
            .catch(error => {
                console.error('Error fetching data:', error);
            });
    }, []);

    return (
        <div>
            <h1>Backend Message:</h1>
            <p>{message}</p>
        </div>
    );
};

export default BackendMessage;
