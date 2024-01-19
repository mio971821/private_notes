// JavaScript source code
// 獲取圖片和標點元素
const image = document.getElementById('image');
const points = document.getElementsByClassName('point');

// 根據窗口大小對圖片和標點進行縮放
function scaleElements() {
    const scaleFactor = Math.min(window.innerWidth / image.naturalWidth, window.innerHeight / image.naturalHeight);
    image.style.width = `${image.naturalWidth * scaleFactor}px`;
    image.style.height = `${image.naturalHeight * scaleFactor}px`;

    for (const point of points) {
        point.style.fontSize = `${10 * scaleFactor}px`;
    }
}

// 在窗大小改變時重新縮放
window.addEventListener('resize', scaleElements);

// 頁面加載完成時執行縮放
window.addEventListener('load', scaleElements);



function initializeMap() {
    const mapOptions = {
        center: { lat: 24.957389635212323, lng: 121.24078411958688 }, // 地圖中心點的緯度和經度
        zoom: 15, // 地圖縮放級別
    };

    // 創建地圖
    const map = new google.maps.Map(document.getElementById('map'), mapOptions);

    // 在地圖上標記選取的點
    

    for (const point of selectedPoints) {
        const marker = new google.maps.Marker({
            position: { lat: point.x, lng: point.y },
            map: map,
            title: point.label,
        });
    }
}

function displayHouses(houses) {
    const mapContainer = document.getElementById('map-container');
    const mapOptions = {
        center: { lat: 24.957, lng: 121.240 }, // 設定地圖中心座標
        zoom: 14, // 設定初始縮放級別
    };
    const map = new google.maps.Map(mapContainer, mapOptions);

    // 在地圖上顯示房屋
    houses.forEach(house => {
        const marker = new google.maps.Marker({
            position: { lat: house.latitude, lng: house.longitude },
            map: map,
            title: house.name,
        });

        const infoWindow = new google.maps.InfoWindow({
            content: `<div><strong>${house.name}</strong><br>${house.distance}<br>${house.duration}</div>`,
        });

        marker.addListener('click', () => {
            infoWindow.open(map, marker);
        });
    });
}

// JavaScript source code
function calculateDistance() {
    const selectedPoints = [];
    // 獲取 checkbox 狀態，並將被選取的點添加到 selectedPoints 陣列
    if (document.getElementById('pointA').checked) {
        selectedPoints.push({ label: '中原大學校門口', x: 24.957389635212323, y: 121.24078411958688 }); //中原大學校門口的座標是 (24.957389635212323, 121.24078411958688)
    }

    if (document.getElementById('pointB').checked) {
        selectedPoints.push({ label: '商學大樓', x: 24.957499456364083, y: 121.24353260587941 }); // 商學大樓的座標是 (24.957499456364083, 121.24353260587941)
    }

    if (document.getElementById('pointC').checked) {
        selectedPoints.push({ label: '化學館', x: 24.957490790963696, y: 121.24273142219266 }); // 化學館的座標是 (24.957490790963696, 121.24273142219266)
    }

    if (document.getElementById('pointD').checked) {
        selectedPoints.push({ label: '理學大樓', x: 24.95754587728386, y: 121.24238711528693 }); // 化學館的座標是 (24.957490790963696, 121.24273142219266)
    }

    if (document.getElementById('pointE').checked) {
        selectedPoints.push({ label: '科學館', x: 24.957747860250983, y: 121.24190103496588 }); // 化學館的座標是 (24.957490790963696, 121.24273142219266)
    }
    if (document.getElementById('pointF').checked) {
        selectedPoints.push({ label: '工學館', x: 24.95730135831001, y: 121.2442884846603 }); // 化學館的座標是 (24.957490790963696, 121.24273142219266)
    }
    if (document.getElementById('pointG').checked) {
        selectedPoints.push({ label: '資管樓', x: 24.9570419581077, y: 121.24352911706401 }); // 化學館的座標是 (24.957490790963696, 121.24273142219266)
    }
    if (document.getElementById('pointH').checked) {
        selectedPoints.push({ label: '商設館', x: 24.956830696761095, y: 121.24391558845609 }); // 化學館的座標是 (24.957490790963696, 121.24273142219266)
    }
    if (document.getElementById('pointI').checked) {
        selectedPoints.push({ label: '土木館', x: 24.95653920328668, y: 121.24474239273533 }); // 化學館的座標是 (24.957490790963696, 121.24273142219266)
    }
    if (document.getElementById('pointJ').checked) {
        selectedPoints.push({ label: '全人教育村', x: 24.958653258288816, y: 121.24207106374845 }); // 化學館的座標是 (24.957490790963696, 121.24273142219266)
    }
    if (document.getElementById('pointK').checked) {
        selectedPoints.push({ label: '工業系館', x: 24.95645772057134, y: 121.24413250445546 }); // 化學館的座標是 (24.957490790963696, 121.24273142219266)
    }
    if (document.getElementById('pointL').checked) {
        selectedPoints.push({ label: '設計學院', x: 24.955797572007363, y: 121.24458338824185 }); // 化學館的座標是 (24.957490790963696, 121.24273142219266)
    }
    if (document.getElementById('pointM').checked) {
        selectedPoints.push({ label: '室設館', x: 24.956114466550556, y: 121.24504942727349 }); // 化學館的座標是 (24.957490790963696, 121.24273142219266)
    }
    if (document.getElementById('pointN').checked) {
        selectedPoints.push({ label: '望樓', x: 24.955735738830644, y: 121.24514320342008 }); // 化學館的座標是 (24.957490790963696, 121.24273142219266)
    }
    if (document.getElementById('pointO').checked) {
        selectedPoints.push({ label: '景觀樓', x: 24.955563121048, y: 121.24477378223646 }); // 化學館的座標是 (24.957490790963696, 121.24273142219266)
    }
    if (document.getElementById('pointP').checked) {
        selectedPoints.push({ label: '建築系館', x: 24.955910064703485, y: 121.24346323622655 }); // 化學館的座標是 (24.957490790963696, 121.24273142219266)
    }
    if (document.getElementById('pointQ').checked) {
        selectedPoints.push({ label: '電學大樓', x: 24.95618975373568, y: 121.24252363754408 }); // 化學館的座標是 (24.957490790963696, 121.24273142219266)
    }
    if (document.getElementById('pointR').checked) {
        selectedPoints.push({ label: '真知教學大樓', x: 24.956111890178626, y: 121.24188377201658 }); // 化學館的座標是 (24.957490790963696, 121.24273142219266)
    }
    if (document.getElementById('pointS').checked) {
        selectedPoints.push({ label: '維澈樓', x: 24.956944632757263, y: 121.24101002324007 }); // 化學館的座標是 (24.957490790963696, 121.24273142219266)
    }
    if (document.getElementById('pointT').checked) {
        selectedPoints.push({ label: '行政大樓', x: 24.95715448226101, y: 121.24168739132654 }); // 化學館的座標是 (24.957490790963696, 121.24273142219266)
    }
    if (document.getElementById('pointU').checked) {
        selectedPoints.push({ label: '張靜愚紀念圖書館', x: 24.95817903644287, y: 121.24064240639197 }); // 化學館的座標是 (24.957490790963696, 121.24273142219266)
    }
    if (document.getElementById('pointV').checked) {
        selectedPoints.push({ label: '恩惠堂', x: 24.957802124253746, y: 121.24324184678167 }); // 化學館的座標是 (24.957490790963696, 121.24273142219266)
    }
    if (document.getElementById('pointW').checked) {
        selectedPoints.push({ label: '生科樓', x: 24.95899361409398, y: 121.24030040644293 }); // 化學館的座標是 (24.957490790963696, 121.24273142219266)
    }
    if (document.getElementById('pointX').checked) {
        selectedPoints.push({ label: '活動中心', x: 24.959005677780105, y: 121.24095425655912 }); // 化學館的座標是 (24.957490790963696, 121.24273142219266)
    }
    if (document.getElementById('pointY').checked) {
        selectedPoints.push({ label: '中壢火車站', x: 24.95374427151194, y: 121.22559928615601 }); // 化學館的座標是 (24.957490790963696, 121.24273142219266)
    }
    if (document.getElementById('pointZ').checked) {
        selectedPoints.push({ label: '中大撞球俱樂部', x: 24.958640773154947, y: 121.23842279570341 }); // 中壢火車站的座標是 (24.95374427151194, 121.22559928615601)
    }
    if (document.getElementById('pointAA').checked) {
        selectedPoints.push({ label: '大潤發_中壢店', x: 24.95426823865471, y: 121.23455536245933 }); // 中壢火車站的座標是 (24.95374427151194, 121.22559928615601)
    }
    if (document.getElementById('pointAB').checked) {
        selectedPoints.push({ label: '中油中壢環中站', x: 24.955309534835536, y: 121.955309534835536 }); // 中壢火車站的座標是 (24.95374427151194, 121.22559928615601)
    }
    if (document.getElementById('pointAC').checked) {
        selectedPoints.push({ label: '家樂福中壢店', x: 24.94709390896928, y: 121.24471397075055 }); // 中壢火車站的座標是 (24.95374427151194, 121.22559928615601)
    }
    if (document.getElementById('pointAD').checked) {
        selectedPoints.push({ label: '家樂福中原店', x: 24.96235732257548, y: 121.23224673654806 }); // 中壢火車站的座標是 (24.95374427151194, 121.22559928615601)
    }
    if (document.getElementById('pointAE').checked) {
        selectedPoints.push({ label: '中原國小停車場', x: 24.95640584730433, y: 121.23937311492917 }); // 中壢火車站的座標是 (24.95374427151194, 121.22559928615601)
    }
    if (document.getElementById('pointAF').checked) {
        selectedPoints.push({ label: '大魯閣棒壘球打擊場_中壢館', x: 24.957859981440862, y: 121.24961632827927 }); // 中壢火車站的座標是 (24.95374427151194, 121.22559928615601)
    }
    if (document.getElementById('pointAG').checked) {
        selectedPoints.push({ label: '大樹藥局', x: 24.952064233809793, y: 121.2401334325744 }); // 中壢火車站的座標是 (24.95374427151194, 121.22559928615601)
    }
    
    const orderButton = document.getElementById("order_money");
    const orderType = orderButton.classList.contains("order_up") ? 'asc' : 'desc';
    var DropdownButtonDiv = document.getElementById('DropdownButton');

    // 檢查 div 是否可見
    var divIsVisible = window.getComputedStyle(DropdownButton).display !== 'none';
    if (divIsVisible) $('#loading-spinner').show();

    $.ajax({
        url: '/welcome/tenant_b/',
        type: 'GET',
        data: {
            selectedPoints: JSON.stringify(selectedPoints),
            ...currentFilters,
            order_type: orderType
        },
        contentType: 'application/json', // 設置請求的 Content-Type
    })
        .done(function (data) {
            // 成功時的處理
            const cardContainer = document.getElementById("card-container");
            cardContainer.innerHTML = '';

            if (data.query_result) {
                data.query_result.forEach((item, index) => {
                    const delay = index * 0.1;
                    createCard(item, delay, index);
                });
            }

            $('#loading-spinner').hide();  // 隱藏 Spinner
        })
        .fail(function (xhr, status, error) {
            // 失敗時的處理
            console.error(error);
            $('#loading-spinner').hide();  // 隱藏 Spinner
        });
}


function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}







