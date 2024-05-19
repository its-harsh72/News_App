import React, { Component } from 'react'
import NewsItem from './NewsItem'
import Spinner from './Spinner';
import PropTypes from 'prop-types';
import InfiniteScroll from "react-infinite-scroll-component";
export class News extends Component {



    static defaultProps = {
        country: "in",
        pageSize: 8,
        category: 'general'


    }
    static propTypes = {
        country: PropTypes.string,
        pageSize: PropTypes.number,
        category: PropTypes.string

    }


    capatalizeFirstLetter = (string) => {
        return string.charAt(0).toUpperCase() + string.slice(1);
    }
    articles = []
    constructor(props) {

        super(props);
        this.state = {
            articles: this.articles,
            page: 1,
            loading: false,
            totalResults:0
        }
        document.title = `${this.capatalizeFirstLetter(this.props.category)} - MemeNews`;
    }
    async componentDidMount() {
        this.props.setProgress(10);
        let url = `https://newsapi.org/v2/top-headlines?country=${this.props.country}&category=${this.props.category}&apiKey=${this.props.apiKey}&page=${this.state.page}&pagesize=${this.props.pageSize}`;
        this.setState({ loading: true })
        this.props.setProgress(30);
        let data = await fetch(url);
        let parseData = await data.json();
        this.props.setProgress(50);
        this.setState({
            articles: parseData.articles, loading: false, totalResults: parseData.totalResults
        })
        this.props.setProgress(100);
        console.log(parseData);
    }

    // handledClickP = async () => {
    //     console.log("I am previous")
    //     let url = `https://newsapi.org/v2/top-headlines?country=${this.props.country}&category=${this.props.category}&apiKey=45f1ed5b71b049e3bd1d532068c9f50a&page=${this.state.page - 1}&pagesize=${this.props.pageSize}`;
    //     this.setState({ loading: true })
    //     let data = await fetch(url);
    //     let parseData = await data.json();
    //     this.setState({
    //         articles: parseData.articles,
    //         page: this.state.page - 1,
    //         loading: false
    //     })
    //     console.log(parseData);

    // }

    // handledClickN = async () => {
    //     if (!(this.state.page + 1 > Math.ceil(this.state.totalResults / 20))) {
    //         let url = `https://newsapi.org/v2/top-headlines?country=${this.props.country}&category=${this.props.category}&apiKey=45f1ed5b71b049e3bd1d532068c9f50a&page=${this.state.page + 1}&pagesize=${this.props.pageSize}`;
    //         this.setState({ loading: true })
    //         let data = await fetch(url);
    //         let parseData = await data.json();
    //         this.setState({
    //             articles: parseData.articles,
    //             page: this.state.page + 1,
    //             loading: false
    //         })
    //         console.log(parseData);
    //     }
    // }
    fetchMoreData = async() => {
        this.setState({page:this.state.page+1});
        let url = `https://newsapi.org/v2/top-headlines?country=${this.props.country}&category=${this.props.category}&apiKey=${this.props.apiKey}&page=${this.state.page+1}&pagesize=${this.props.pageSize}`;
        this.setState({ loading: true })
        let data = await fetch(url);
        let parseData = await data.json();
        this.setState({
            articles: this.state.articles.concat(parseData.articles), 
            loading: false, 
            totalResults: parseData.totalResults
        })
      };
    render() {

        return (
            <div className="container my-3">
                <h1 className="col text-center">Meme-News - Top {this.capatalizeFirstLetter(this.props.category)} Headlines</h1>
                {/* {this.state.loading && <Spinner/>} */}
                <InfiniteScroll
                    dataLength={this.state.articles.length}
                    next={this.fetchMoreData}
                    hasMore={this.state.articles.length!== this.state.totalResults}
                    loader={<Spinner/>}
                >
                    <div className="container">
                    <div className="row">
                        {this.state.articles.map((element) => {
                            return (
                                <div className="col-md-4 my-2" key={element.url}>
                                    <NewsItem
                                        title={element.title?.slice(0, 35)}
                                        description={element.description?.slice(0, 88)}
                                        imageUrl={element.urlToImage}
                                        newaUrl={element.url}
                                        author={element.author}
                                        source={element.source.name}
                                        publishedAt={element.publishedAt}
                                    />
                                </div>
                            );
                        })}
                    </div>
                    </div>
                </InfiniteScroll>
                <div className="d-flex justify-content-between">
                    <button disabled={this.state.page <= 1} type="button" className="btn btn-dark" onClick={this.handledClickP}>&larr;Previous Page</button>

                    <button disabled={this.state.page + 1 > Math.ceil(this.state.totalResults / 20)} type="button" className="btn btn-dark" onClick={this.handledClickN}>Next Page &rarr;</button>
                </div>
            </div>
        );
    }
}

export default News
