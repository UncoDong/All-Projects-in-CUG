document.addEventListener("DOMContentLoaded", function () {

    document.getElementById("prev").addEventListener("click", function () {
        var current = document.getElementsByClassName("current")[0];
        var id = parseInt(current.id);
        var nextId = (id - 1)
        if (id == 1) {
            nextId = 5
        }
        console.log(nextId);
        current.className = "ball";
        document.getElementById('' + nextId).className = "ball current";
        flush();
    });

    document.getElementById("next").addEventListener("click", function () {
        var current = document.getElementsByClassName("current")[0];
        var id = parseInt(current.id);
        var nextId = id + 1;
        if (id == 5) {
            nextId = 1
        }
        console.log(nextId);
        current.className = "ball";
        document.getElementById('' + nextId).className = "ball current";
        flush();
    });

    for (i = 1; i <= 5; i++) {
        document.getElementById('' + i).addEventListener("click", function () {
            for (i = 1; i <= 5; i++) {
                if (this.id == '' + i) {
                    this.className = "ball current";
                }
                else {
                    document.getElementById('' + i).className = "ball";
                }
            }
            flush();
        })
    }

    let flush = () => {
        var current = document.getElementsByClassName('current')[0];
        var id = parseInt(current.id);
        document.getElementById('img').src = '/static/img/预览' + id + '.png';

    };
    function next() {
        document.getElementById('next').click();
    }
    setInterval(next, 3000);


});
