

/* console.log.에 Promise<pending> 으로 값이 안나타남. */

var webdriver = require('selenium-webdriver');
var chrome = require('selenium-webdriver/chrome');
var chromedriver = require('chromedriver');
var By = require('selenium-webdriver').By;
var cheerio = require('cheerio');
var axios = require('axios');


var url = 'https://dtpia.co.kr/Order/Businesscard/Color.aspx';
//var url = 'https://www.myprotein.co.kr/your-goals/muscle-and-strength-range.list';

// chrome.setDefaultService(new chrome.ServiceBuilder(chromedriver.path).build());



var driver = new webdriver.Builder()
    .withCapabilities(webdriver.Capabilities.chrome())
    .build();


    // driver.get('http://www.google.com');
    // var searchForm = driver.findElement(By.tagName('form'));
    // var searchBox = searchForm.findElement(By.name('q'));
    // searchBox.sendKeys('webdriver');


    // driver.get(url);
    // //var searchForm = driver.findElement(By.tagName('form'));
    // var searchBox = driver.findElement(By.name('title'));
    // searchBox.sendKeys('webdriver');


/*
var hrefList = new Array();
var srcList = new Array();

var maxPage = driver.findElement(By.xpath(
    '//*[@id="clothing-women-trousers-shorts"]/div/section/section/section/div[2]/div[2]/div[2]/div[2]/div/div/nav/div/a[3]'
));

maxPage.then(function (value){
    value.getText().then(function (maxPage){
        console.log('마지막번호 : ', maxPage);
        return maxPage
    }).then(function(maxPage){
        console.log('가져온 마지막 페이지 번호 : ', maxPage)
    })
})
*/



// (async function example() {
//     //let driver = await new Builder().withCapabilities(webdriver.Capabilities.chrome()).build();
//     let driver = new webdriver.Builder()
//      .withCapabilities(webdriver.Capabilities.chrome())
//      .build();

//     try {
//       await driver.get(url);
//       let tag = await driver.findElement(By.name('page_code'));
//       console.log('tag : ', tag.getText());
//       //await driver.findElement(By.name('q')).sendKeys('webdriver');
//       //await driver.wait(until.titleIs('webdriver - Google Search'), 1000);
//     } finally {
//       await driver.quit();
//     }
//   })();






const main = async () => {
    try {
        console.log('main_async()')
        driver.get(url)
        let tag = await driver.findElement({name : 'page_code'}).then(function (ee){
            //console.log('tag : ', tag.getText());   
            console.log('tag111 : ', ee.getText());    
        });
        //console.log('tag22 : ', tag.getText());

        return tag;

    } catch (error) {
        console.log('err : ', error);
    }
}

main().then(value => {
    console.log('value', value)
})











//let test = main();


//console.log('test : ', test);

// test.then((value) => {
//     console.log('value : ', value);
// })





//let tag = '';

//driver.get(url)
    /*
    .then(function(){
        tag = driver.findElement(By.name('page_code'));
        console.log('tag : ', tag.getText());
        return tag; 
    })
    */










/*
async function elementValue () {
    await driver.get(url)
    let tag = await driver.findElement(By.name('page_code'));
    console.log('tag : ', tag.getText());
    return tag;
}

elementValue().then(function (value){
    console.log('value : ', value.getText())
});

*/







//let tag = driver.findElement(By.name('page_code'));
//console.log('tag : ', tag.getText());

//const data = await elementValue();
//console.log('data : ', data);

// tag.getText().then(function (value){
//     console.log('tag1 : ', value);
// })

// tag.then(function (value) {
//     console.log('tag2 : ' + value.getText())
// });










// var driver = new webdriver.Builder()
//    .forBrowser('chrome').build();
// driver.get(url);

// var driver = new webdriver.Builder()
//   .forBrowser('chrome')
//   .build();
// driver.get('https://google.com');




/*

const driver = new webdriver.Builder()
  // 작동하고 있는 크롬 드라이버의 포트 "9515"를 사용합니다.
  .usingServer('http://localhost:9515')
  .withCapabilities({
    chromeOptions: {
      // 여기에 사용중인 Electron 바이너리의 경로를 지정하세요.
      binary: '/Path-to-Your-App.app/Contents/MacOS/Electron'
    }
  })
  .forBrowser('electron')
  .build()

driver.get('http://www.google.com')
driver.findElement(webdriver.By.name('q')).sendKeys('webdriver')
driver.findElement(webdriver.By.name('btnG')).click()
driver.wait(() => {
  return driver.getTitle().then((title) => {
    return title === 'webdriver - Google Search'
  })
}, 1000)

driver.quit()

*/