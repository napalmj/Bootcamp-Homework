function toggleEdit(){
    let formContainer = document.getElementById("myToggle");
    if (formContainer.style.display === 'none'){
        formContainer.style.display = 'block';
    } else {
        formContainer.style.display = 'none';
    }
}

function getEditInfo(vars){
    let editInfo = vars
    console.log(vars)
}

// onclick="toggleEdit(); getEditInfo(dataString); return false;"