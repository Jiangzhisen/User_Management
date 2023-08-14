//update user
$(".click2").click(function() {
    const email2 = $("#email2").val()
    const password2 = $("#password2").val()
    const priority2 = $("#priority2").val()

    console.log(email2)
    console.log(password2)
    console.log(priority2)

    let headers = {
        "Content-Type": "application/json"
    };

    let body = {
        "email": email2,
        "password": password2,
        "priority": priority2
    };

    let url = `http://127.0.0.1:5000/user/update`;
    fetch(url, {method: 'POST', headers: headers, body: JSON.stringify(body)})
    .then(res => {
        return res.json();
    })
    .then(result => {
        console.log(result);

        $("#updateContainer").empty();
        if(email2 != '' && password2 != '' || priority2 != '') {
            const row = `
            <div class="container mt-5">
                <div class="row align-items-center">
                    <div class="col text-center">Successfully Update!!</div>
                </div>
            </div>`;
            $("#updateContainer").append(row);

            const emailCol = `
            <div class="row align-items-center">
                <div class="col text-center">
                    <label for="staticEmail" class="col-sm-2 col-form-label">Email</label>
                </div>
                <div class="col text-center">${email2}</div>
            </div>`;
            const passwordCol = `
            <div class="row align-items-center">
                <div class="col text-center">
                    <label for="staticPassword" class="col-sm-2 col-form-label">Password</label>
                </div>
                <div class="col text-center">${password2}</div>
            </div>`;
            const priorityCol = `
            <div class="row align-items-center">
                <div class="col text-center">
                    <label for="staticPriority" class="col-sm-2 col-form-label">Priority</label>
                </div>
                <div class="col text-center">${priority2}</div>
            </div>`;
            const container = `
            <div class="container mt-5">
                ${emailCol}
                ${passwordCol}
                ${priorityCol}
            </div>`;
            $("#updateContainer").append(container);
            // const row = `<p>successfully update!!</p>`;
            // const row1 = `<p>Email: ${email2} Password: ${password2} Priority: ${priority2}</p>`;
            // $("#updateContainer").append(row);
            // $("#updateContainer").append(row1);
        }
        else {
            const row = `<p>please input complete!!!!</p>`;
            $("#updateContainer").append(row);
        }
    })
    .catch(err => {
        console.log(err);
        const row1 = `<p>update failed!!</p>`;
        $("#updateContainer").append(row1);
    })
});