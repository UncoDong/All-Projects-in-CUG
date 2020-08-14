
document.addEventListener("DOMContentLoaded", function () {

    let speed = 60, //节拍速度
        arrClick = [],  //测速时每次点击的速度组成的数组，节拍速度取其平均值
        clickTime = 0,  //测速点击计时器，超过 3 秒清空数组
        s = Date.now(), //记录每一次点击的时间，下一次点击时与此时间的间隔，来计算速度
        time = 0,   //play 过程 timeout 变量
        isPlay = false, //是否正在播放
        speedMsg = document.getElementById("speed"),    //页面正中间显示速度值的元素
        rangeValue = document.getElementById("rangeValue"), //滑块元素
        showSpeed = () => rangeValue.value = speedMsg.innerText = speed;    //更新显示速度值的函数

    /** 测速按钮点击 */
    document.getElementById("btnTest").addEventListener("click", function () {
        let lastSpeed = Math.floor(60000 / (Date.now() - s));
        if (lastSpeed - arrClick[arrClick.length - 1] > 30) { arrClick = []; }  //如果点击时间和上次差别较大，则清零重测
        arrClick.push(lastSpeed);

        if (arrClick.length > 31) arrClick.shift(); //最大容量保持在30个（除去第 1 个不用）

        //如果数量多于1个则计算速度（第 1 个时间间隔太久，不准确，弃之）
        if (arrClick.length > 1) {
            //取第2个到最后的平均值
            speed = Math.ceil((arrClick.reduce((sum, n) => sum + n) - arrClick[0]) / (arrClick.length - 1));
            if (arrClick.length > 5) document.getElementById("msg").innerText = "多点几次更准确...";
        }
        showSpeed();
        s = Date.now();
        document.getElementById("btnStop").click(); //测速时停止播放

        //两次点击间隔大于 3 秒就重置
        window.clearTimeout(clickTime);
        clickTime = window.setTimeout(function () {
            arrClick = [];
            document.getElementById("msg").innerText = "";
        }, 3000);

    });
    var btn = 0;
    /** 播放按钮点击 */
    document.getElementById("btnPlay").addEventListener("click", function () {
        var BTN = document.getElementById("btnPlay");
        if (btn % 2 == 0) {
            isPlay = true;
            play();
            BTN.innerHTML = "停止"
            btn++;
        }
        else {
            window.clearTimeout(time);
            isPlay = false;
            BTN.innerHTML = "开始"
            btn++;
        }

    });


    /** 减号按钮点击 */
    document.getElementById("btnSub").addEventListener("click", function () {
        speed--;
        showSpeed();
    });

    /** 加号按钮点击 */
    document.getElementById("btnAdd").addEventListener("click", function () {
        speed++;
        showSpeed();
    });

    /** 滑动条更改 */
    rangeValue.addEventListener("change", function () {
        speed = this.value * 1;
        showSpeed();
    });

    /** 播放 */
    let play = () => {
        window.clearTimeout(time);
        playsound();
        if (isPlay) {
            time = window.setTimeout(play, Math.floor(60000 / speed));
        };
    }

    let audioCtx = new AudioContext();
    /** 发声 */
    let playsound = () => {
        let oscillator = audioCtx.createOscillator();
        let gainNode = audioCtx.createGain();
        oscillator.connect(gainNode);
        gainNode.connect(audioCtx.destination);
        oscillator.type = 'sine';
        oscillator.frequency.setValueAtTime(220, audioCtx.currentTime);
        oscillator.frequency.linearRampToValueAtTime(50, audioCtx.currentTime + 0.1);
        gainNode.gain.setValueAtTime(0, audioCtx.currentTime);
        gainNode.gain.linearRampToValueAtTime(1, audioCtx.currentTime + 0.01);
        gainNode.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + 0.5);
        oscillator.start(audioCtx.currentTime);
        oscillator.stop(audioCtx.currentTime + 0.5);
    }
});