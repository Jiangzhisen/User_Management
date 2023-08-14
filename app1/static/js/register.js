 //create user
 $(".click1").click(function() {
    const email1 = $("#email1").val()
    const password1 = $("#password1").val()
    const priority1 = $("#priority1").val()

    let headers = {
        "Content-Type": "application/json"
    };

    let body = {
        "email": email1,
        "password": password1,
        "priority": priority1
    };

    let url = `http://127.0.0.1:5000/user/create`;
    fetch(url, {method: 'POST', headers: headers, body: JSON.stringify(body)})
    .then(res => {
        return res.json();
    })
    .then(result => {
        console.log(result);

        $("#createContainer").empty();
        if (email1 != '' && password1 != '' && priority1 != '') {
            const row = `
            <div class="container mt-5">
                <div class="row align-items-center">
                    <div class="col text-center">Successfully Register!!</div>
                </div>
            </div>`;
            $("#createContainer").append(row);
        
            const emailCol = `
            <div class="row align-items-center">
                <div class="col text-center">
                    <label for="staticEmail" class="col-sm-2 col-form-label">Email</label>
                </div>
                <div class="col text-center">${email1}</div>
            </div>`;
            const passwordCol = `
            <div class="row align-items-center">
                <div class="col text-center">
                    <label for="staticPassword" class="col-sm-2 col-form-label">Password</label>
                </div>
                <div class="col text-center">${password1}</div>
            </div>`;
            const priorityCol = `
            <div class="row align-items-center">
                <div class="col text-center">
                    <label for="staticPriority" class="col-sm-2 col-form-label">Priority</label>
                </div>
                <div class="col text-center">${priority1}</div>
            </div>`;
            const backBtn = `
            <div class="row align-items-center"></div>
            <div class="row align-items-center">
                <div class="col text-center">
                    <a href="/login" class="btn btn-primary">Back to login</a>
                </div>
            </div>`;
        
            const container = `
            <div class="container mt-5">
                ${emailCol}
                ${passwordCol}
                ${priorityCol}
                ${backBtn}
            </div>`;
            
            $("#createContainer").append(container);
        }        
        else {
            const row = `<p>Please input complete!!!!</p>`;
            $("#createContainer").append(row);
        }
    })
    .catch(err => {
        console.log(err);
        const row1 = `<p>Register failed!!</p>`;
        $("#createContainer").append(row1);
    })
});