 //search user
 $(".click").click(function() {
    const email = $("#email").val();
    const priority = $("#priority").val();


    let headers = {
        "Content-Type": "application/json"
    };

    let body = {
        "email": email,
        "priority": priority
    };

    console.log(body)

    let url = `http://127.0.0.1:5000/user/detail`;
    fetch(url, {method: 'POST', headers: headers, body: JSON.stringify(body)})
    .then(res => {
        return res.json();
    })
    .then(result => {
        console.log(result);

        $("#searchContainer").empty();
        if(email != '' || priority != '') {
            const row1 = `<div>Email&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;Password&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;Priority</div>`;
            $("#searchContainer").append(row1);
            result.forEach(item => {
                const emailInput = `<input type="text" class="emailinfo" value="${item.user_email}" readonly>`;
                const passwordInput = `<input type="text" class="passwordinfo" value="${item.user_password}" readonly>`;
                const priorityInput = `<input type="text" class="priorityinfo" value="${item.user_priority}" readonly>`;
                const row = `<div>${emailInput}${passwordInput}${priorityInput}</div>`;
                $("#searchContainer").append(row);
            });
        }
        else {
            const row = `<p>please input complete!!!!</p>`;
            $("#searchContainer").append(row);
        }

    })
    .catch(err => {
        console.log(err);
    })
});


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
        if(email1 != '' && password1 != '' && priority1 != '') {
            const row = `<p>successfully create!!</p>`;
            const row1 = `<p>Email: ${email1} Password: ${password1} Priority: ${priority1}</p>`;
            $("#createContainer").append(row);
            $("#createContainer").append(row1);
        }
        else {
            const row = `<p>please input complete!!!!</p>`;
            $("#createContainer").append(row);
        }
    })
    .catch(err => {
        console.log(err);
        const row1 = `<p>create failed!!</p>`;
        $("#createContainer").append(row1);
    })
});


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
            const row = `<p>successfully update!!</p>`;
            const row1 = `<p>Email: ${email2} Password: ${password2} Priority: ${priority2}</p>`;
            $("#updateContainer").append(row);
            $("#updateContainer").append(row1);
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


//delete user
$(".click3").click(function() {
    const email3 = $("#email3").val()

    console.log(email3)

    let headers = {
        "Content-Type": "application/json"
    };

    let body = {
        "email": email3,
    };

    let url = `http://127.0.0.1:5000/user/delete`;
    fetch(url, {method: 'POST', headers: headers, body: JSON.stringify(body)})
    .then(res => {
        return res.json();
    })
    .then(result => {
        console.log(result);

        $("#deleteContainer").empty();
        if(email3 != '') {
            const row = `<p>successfully delete!!</p>`;
            const row1 = `<p>Email: ${email3}`;
            $("#deleteContainer").append(row);
            $("#deleteContainer").append(row1);
        }
        else {
            const row = `<p>please input complete!!!!</p>`;
            $("#deleteContainer").append(row);
        }
    })
    .catch(err => {
        console.log(err);
        const row1 = `<p>delete failed!!</p>`;
        $("#deleteContainer").append(row1);
    })
});