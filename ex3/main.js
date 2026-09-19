/* ============================================================
 *  我的第一个地理信息服务 —— 主脚本
 *  依赖：Leaflet 1.0.2、jQuery 3.x、heatmap.js、leaflet-heatmap 1.x
 *  功能：天地图 DataServer（EPSG:3857 Web Mercator）矢量/影像底图切换
 *       + 热力图 + 标记点
 *
 *  天地图两种接口：
 *    WMTS 格式（复杂，容易出问题）：
 *      /vec_w/wmts?service=wmts&request=GetTile&version=1.0.0...
 *    DataServer 格式（简洁，推荐，实测有效）：
 *      /DataServer?T=vec_w&x={x}&y={y}&l={z}&tk=xxx
 *
 *  两个投影：
 *    _w 后缀 → EPSG:3857 Web Mercator，和 Leaflet 默认 CRS 对齐
 *    _c 后缀 → EPSG:4326 地理坐标系，需要 crs: L.CRS.EPSG4326
 * ============================================================ */

/* ------------------------------------------------------------
 *  1. 天地图 DataServer 瓦片 URL
 *     使用 DataServer 接口（比 WMTS 稳定得多）
 *     统一用 _w 后缀 → EPSG:3857，和 Leaflet 默认 CRS 对齐
 *     token：20a2a42bdf6b7a5c648af796cf2c9105（公开示例 key）
 *     如果失效，请到 https://console.tianditu.gov.cn/ 申请自己的
 * ------------------------------------------------------------ */
var TIANDITU_TK = '20a2a42bdf6b7a5c648af796cf2c9105';

var tileUrl = {
    // 矢量底图
    vec: 'https://t{s}.tianditu.gov.cn/DataServer?T=vec_w&x={x}&y={y}&l={z}&tk=' + TIANDITU_TK,
    // 矢量注记
    cva: 'https://t{s}.tianditu.gov.cn/DataServer?T=cva_w&x={x}&y={y}&l={z}&tk=' + TIANDITU_TK,
    // 影像底图
    img: 'https://t{s}.tianditu.gov.cn/DataServer?T=img_w&x={x}&y={y}&l={z}&tk=' + TIANDITU_TK,
    // 影像注记
    cia: 'https://t{s}.tianditu.gov.cn/DataServer?T=cia_w&x={x}&y={y}&l={z}&tk=' + TIANDITU_TK
};

// subdomains 0~7，URL 模板 https://t{s} 会拼成 t0 ~ t7
var SUBDOMAINS = ['0', '1', '2', '3', '4', '5', '6', '7'];

// 当前底图类型：Vec = 矢量，Sat = 影像
var curMapModel = "Vec";

/* ------------------------------------------------------------
 *  2. 初始化地图
 *     没有指定 crs → 默认 EPSG:3857，和上面的 _w 后缀对齐
 * ------------------------------------------------------------ */
var map = L.map('mapid', {
    center: [34.607181, 119.2197133],
    zoom: 15,
    maxZoom: 18,
    zoomControl: true,
    attributionControl: false
});

// 初始化时加载矢量底图 + 矢量注记
var baseLayer = L.tileLayer(tileUrl.vec, { subdomains: SUBDOMAINS }).addTo(map);
var lablayer = L.tileLayer(tileUrl.cva, { subdomains: SUBDOMAINS }).addTo(map);

/* ------------------------------------------------------------
 *  3. 热力图数据（楼盘访问/关注度计数）
 * ------------------------------------------------------------ */
var testData = {
    max: 13000,
    data: [
        { lat: 34.62176, lng: 119.214736, count: 10285 },
        { lat: 34.61498, lng: 119.210096, count: 10204 },
        { lat: 34.59902, lng: 119.222416, count: 10508 },
        { lat: 34.59898, lng: 119.210984, count: 9041 },
        { lat: 34.591312, lng: 119.221184, count: 7442 },
        { lat: 34.607992, lng: 119.204112, count: 12634 },
        { lat: 34.601408, lng: 119.20216, count: 8280 },
        { lat: 34.607181, lng: 119.2197133, count: 2282 }
    ]
};

var heatCfg = {
    radius: 0.008,
    maxOpacity: 0.8,
    scaleRadius: true,
    useLocalExtrema: true,
    latField: 'lat',
    lngField: 'lng',
    valueField: 'count'
};

var heatmapLayer = new HeatmapOverlay(heatCfg);
map.addLayer(heatmapLayer);
heatmapLayer.setData(testData);

/* ------------------------------------------------------------
 *  4. 标记点 —— 各个楼盘
 * ------------------------------------------------------------ */
L.marker([34.62176, 119.214736]).addTo(map)
    .bindPopup("四季金辉");
L.marker([34.61498, 119.210096]).addTo(map)
    .bindPopup("秀逸苏杭");
L.marker([34.59902, 119.222416]).addTo(map)
    .bindPopup("水木华园");
L.marker([34.59898, 119.210984]).addTo(map)
    .bindPopup("一品国际");
L.marker([34.591312, 119.221184]).addTo(map)
    .bindPopup("水木华园");
L.marker([34.607992, 119.204112]).addTo(map)
    .bindPopup("同科汇丰国际");

// 江苏海洋大学标记点 + 500m 圆形范围
L.marker([34.607181, 119.2197133]).addTo(map)
    .bindPopup("<b>江苏海洋大学</b><br />我是一个点").openPopup();

L.circle([34.607181, 119.2197133], 500, {
    color: 'red',
    fillColor: '#f03',
    fillOpacity: 0.5
}).addTo(map).bindPopup("学校范围（500m）");

/* ------------------------------------------------------------
 *  5. 切换底图功能 —— 点击在 矢量 ↔ 影像 之间切换
 * ------------------------------------------------------------ */
function switchlayer() {
    if (curMapModel == "Vec") {
        // 切到影像底图
        baseLayer.setUrl(tileUrl.img);
        lablayer.setUrl(tileUrl.cia);
        curMapModel = "Sat";

        $('.mswitch span').text("地图");
        $('.mswitch').addClass('sat');
    } else if (curMapModel == "Sat") {
        // 切回矢量底图
        baseLayer.setUrl(tileUrl.vec);
        lablayer.setUrl(tileUrl.cva);
        curMapModel = "Vec";

        $('.mswitch span').text("卫星");
        $('.mswitch').removeClass('sat');
    }
}

// 鼠标悬停：加深 span 背景
function swover() {
    $(".mswitch span").css("background-color", "blue");
    $(".mswitch span").css("color", "white");
}

// 鼠标移出：还原 CSS 默认样式
function swout() {
    $(".mswitch span").css("background-color", "");
    $(".mswitch span").css("color", "");
}
