const d = document;

const $body = d.body;
const $fragment = d.createDocumentFragment();
const $temp = d.getElementById("template-card").content;

const response = [
    {
        tag: "h1",
        title: "1",
        content: "Comentario del titulo H1"
    },
    {
        tag: "h2",
        title: "2",
        content: "Comentario del titulo H2"
    },
    {
        tag: "h3",
        title: "3",
        content: "Comentario del titulo H3"
    },
    {
        tag: "h4",
        title: "4",
        content: "Comentario del titulo H4"
    },
    {
        tag: "h5",
        title: "5",
        content: "Comentario del titulo H5"
    },
    {
        tag: "h6",
        title: "6",
        content: "Comentario del titulo H6"
    },
]

response.forEach(e=>{
    const tag = d.createElement(e.tag)
    const $clone = $temp.cloneNode(true);
    $clone.querySelector(".title").textContent = e.title;
    $clone.querySelector(".second-item").textContent = e.content;



    tag.appendChild($clone.querySelector(".title"));
    tag.appendChild($clone.querySelector(".second-item"));
    $fragment.appendChild(tag);
})

$body.appendChild($fragment);