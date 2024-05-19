import Navbar from './Components/Navbar';
import News from './Components/News';
import './App.css';
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import LoadingBar from 'react-top-loading-bar'
import React, { Component } from 'react'

export class App extends Component {
  pageSize=5;
  apiKey=process.env.REACT_APP_NEWS_API
  state={
    progress:10
  }
  setProgress=(progress)=>{
    this.setState({progress:progress})
  }
  render() {
    return (
          <div>
            <Router>
              <Navbar />
              <LoadingBar
              color='#f11946'
              progress={this.state.progress}
            />
              <Routes>
              <Route exact path="/" element={<News setProgress={this.setProgress} apiKey={this.apiKey} key="business"pageSize={6} country="in" category="business" />} />
              <Route exact path="/general" element={<News setProgress={this.setProgress} apiKey={this.apiKey} key="general"pageSize={6} country="in" category="general" />} />
                <Route exact path="/business" element={<News setProgress={this.setProgress} apiKey={this.apiKey} key="business"pageSize={6} country="in" category="business" />} />
                <Route exact path="/entertainment" element={<News setProgress={this.setProgress} apiKey={this.apiKey} key="entertainment" pageSize={6} country="in" category="entertainment" />} />
                <Route exact path="/health" element={<News setProgress={this.setProgress} apiKey={this.apiKey} key="health" pageSize={6} country="in" category="health" />} />
                <Route exact path="/science" element={<News setProgress={this.setProgress} apiKey={this.apiKey} key="science" pageSize={6} country="in" category="science" />} />
                <Route exact path="/sports" element={<News setProgress={this.setProgress} apiKey={this.apiKey} key="sports" pageSize={6} country="in" category="sports" />} />
                <Route exact path="/technology" element={<News setProgress={this.setProgress} apiKey={this.apiKey} key="technology" pageSize={6} country="in" category="technology" />} />
              </Routes>
            </Router>
          </div>
        
      
    )
  }
}




export default App;
