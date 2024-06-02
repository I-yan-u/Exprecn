// import React from 'react'
import PropTypes from 'prop-types'
import style from './css/Modal.module.css'

function Modal({children, onClose}) {
    const handleExit = (e) => {
        if (e.target.className.includes(style.bg)) {
            onClose();
        }
    }

    return (
    <div className={style.bg} onClick={e => handleExit(e)}>
        <div className={style.container} onClick={e => e.stopPropagation()}>
            {children}
        </div>
    </div>
    )
}

Modal.propTypes = {
    children: PropTypes.node,
    onClose: PropTypes.func.isRequired
}

export default Modal;