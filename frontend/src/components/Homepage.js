import React from "react";
import SectionHeader from "./SectionHeader";
import Leaf from "../assets/Leaf.svg";
import SingleLineGridList from "./SingleLineGridList";

const Homepage = () => {
  const tileData = [
    {
      id: 1,
      img:
        "https://storage.googleapis.com/gopasar.appspot.com/media/uploads/product/2020/05/25/IMG_2927_fymetsfc.jpg",
      title: "Image",
      author: "author"
    },
    {
      id: 2,
      img:
        "https://storage.googleapis.com/gopasar.appspot.com/media/uploads/product/2020/05/25/IMG_2927_fymetsfc.jpg",
      title: "Image",
      author: "author"
    },
    {
      id: 3,
      img:
        "https://storage.googleapis.com/gopasar.appspot.com/media/uploads/product/2020/05/25/IMG_2927_fymetsfc.jpg",
      title: "Image",
      author: "author"
    },
    {
      id: 4,
      img:
        "https://storage.googleapis.com/gopasar.appspot.com/media/uploads/product/2020/05/25/IMG_2927_fymetsfc.jpg",
      title: "Image",
      author: "author"
    }
  ];

  return (
    <div>
      <p image={Leaf}>Homepage</p>
      <SectionHeader image={Leaf} alt="leaf" title="Featured" />
      <SingleLineGridList data={tileData} />
    </div>
  );
};

export default Homepage;
