<template>
    <el-carousel height="500px" direction="vertical" :autoplay="false">
      <el-carousel-item v-for="item in 4" :key="item">
        <h3 text="2xl" justify="center">
            <el-image style="width: 1300px; height: 500px" src="https://cube.elemecdn.com/6/94/4d3ea53c084bad6931a56d5158a48jpeg.jpeg" fit="fill" />
        </h3>
    </el-carousel-item>
    </el-carousel>
  </template>
  
  <style scoped>
  .el-carousel__item h3 {
    color: #475669;
    opacity: 0.75;
    line-height: 200px;
    margin: 0;
    text-align: center;
  }
  
  .el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
  }
  
  .el-carousel__item:nth-child(2n + 1) {
    background-color: #d3dce6;
  }
  </style>