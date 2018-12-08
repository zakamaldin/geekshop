const renderItem = ({ title }, count) => (
    `
    <div class="product-item" style="margin-left: 50px">
        <span class="product-item__title">${title}</span>
        <span class="product-item__count">${count}</span>
    </div>
    `
);