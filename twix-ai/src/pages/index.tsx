// twix-ai-frontend/src/pages/index.tsx
import React from 'react';
import BackendMessage from '../components/BackendMessage';

const HomePage: React.FC = () => {
    return (
        <div>
            <h1>Welcome to Twix AI Frontend</h1>
            <BackendMessage />
        </div>
    );
};

export default HomePage;
