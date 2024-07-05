import {createContext, useState} from 'react'
import PropTypes from 'prop-types'

const formDataContext = createContext();

function FormDataContext({children}) {
        const [formData, setFormData] = useState({
                action: 'transcribe',
                reverseTranscribe: 'false',
                methionine: true,
                listView: true,
        });

        const [resultData, setResultData] = useState({})

    return (
        <formDataContext.Provider value={{formData, setFormData, resultData, setResultData}}>
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