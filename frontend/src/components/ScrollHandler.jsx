import {useState, useEffect, createContext} from 'react';

const PageHeight = createContext();

// eslint-disable-next-line react/prop-types
export function ScrollHandler({children}) {
    const [height, setHeight] = useState(0);
    useEffect(() => {
        const updateScrollPosition = () => {
            setHeight(window.scrollY);
        };

        window.addEventListener('scroll', updateScrollPosition);

        return () => window.removeEventListener('scroll', updateScrollPosition);
    }, []);

    return (
        <PageHeight.Provider value={height}>
        {children}
        </PageHeight.Provider>
    )
}

export default PageHeight;