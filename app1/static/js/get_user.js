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
            const row = 
            `<div class="container mt-5">
                <div class="row align-items-center">
                    <div class="col text-center">Email</div>
                    <div class="col text-center">Password</div>
                    <div class="col text-center">Priority</div>
                </div>
            </div>`;
            $("#searchContainer").append(row);
            result.forEach(item => {
                const emailCol = `<div class="col text-center">${item.user_email}</div>`
                // const emailInput = `<input type="text" class="emailinfo" value="${item.user_email}" readonly>`;
                const passwordCol = `<div class="col text-center">${item.user_password}</div>`
                // const passwordInput = `<input type="text" class="passwordinfo" value="${item.user_password}" readonly>`;
                const priorityCol = `<div class="col text-center">${item.user_priority}</div>`
                // const priorityInput = `<input type="text" class="priorityinfo" value="${item.user_priority}" readonly>`;
                const container = `<div class="container mt-5"><div class="row align-items-center">${emailCol}${passwordCol}${priorityCol}</div></div>`;
                $("#searchContainer").append(container);
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