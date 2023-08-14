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
            const row = `
            <div class="container mt-5">
                <div class="row align-items-center">
                    <div class="col text-center">Successfully Delete!!</div>
                </div>
            </div>`;
            $("#deleteContainer").append(row);
            const emailCol = `
            <div class="row align-items-center">
                <div class="col text-center">
                    <label for="staticEmail" class="col-sm-2 col-form-label">Email</label>
                </div>
                <div class="col text-center">${email3}</div>
            </div>`;
            const container = `
            <div class="container mt-5">
                ${emailCol}
            </div>`;
            $("#deleteContainer").append(container);
            // const row = `<p>successfully delete!!</p>`;
            // const row1 = `<p>Email: ${email3}`;
            // $("#deleteContainer").append(row);
            // $("#deleteContainer").append(row1);
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