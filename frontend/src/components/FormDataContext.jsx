import {createContext, useState} from 'react'
import PropTypes from 'prop-types'

const formDataContext = createContext();

function FormDataContext({children}) {
        const [formData, setFormData] = useState({
                action: 'transcription',
                reverseTranscribe: 'false',
                methionine: false,
                listView: false,
        });

    return (
        <formDataContext.Provider value={{formData, setFormData}}>
            {children}
        </formDataContext.Provider>
    )
}

FormDataContext.propTypes = {
    children: PropTypes.node
}

export {
    FormDataContext,
    // eslint-disable-next-line react-refresh/only-export-components
    formDataContext
}