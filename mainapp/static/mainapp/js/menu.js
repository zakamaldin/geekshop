const Category = ({title}) => (
    `<li class="menu_item">
       <h2>
            ${title}
       </h2>
    </li>`
)
const renderCategoryData = res => {
    menuHtml = res.data.results.map(Category)
        .join('')
    menu = document.getElementById('menu_categories')
    menu.innerHTML += menuHtml
}

const Product = ({name}) => (
    `<li class="menu_item">
       <h2>
            ${name}
       </h2>
    </li>`
)
const renderProductData = res => {
    menuHtml = res.data.results.map(Product)
        .join('')
    menu = document.getElementById('menu_categories')
    menu.innerHTML += menuHtml
}