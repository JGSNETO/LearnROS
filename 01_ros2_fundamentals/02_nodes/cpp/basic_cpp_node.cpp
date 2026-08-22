// ============================================================
// ROS 2 C++ Node - Basic Template
// ============================================================

// Include the ROS 2 C++ client library
#include "rclcpp/rclcpp.hpp"


// ============================================================
// Node Class
// ============================================================

class MyNode : public rclcpp::Node
{
public:

    MyNode()
        // Initialize the ROS 2 node
        // The argument is the node name
        : Node("my_cpp_node")
    {
        // ----------------------------------------------------
        // Create publishers, subscribers, timers, services,
        // parameters, etc. here.
        // ----------------------------------------------------

        // Example:
        //
        // timer_ = this->create_wall_timer(
        //     std::chrono::seconds(1),
        //     std::bind(
        //         &MyNode::timer_callback,
        //         this
        //     )
        // );

        RCLCPP_INFO(
            this->get_logger(),
            "C++ node started!"
        );
    }


private:

    // ========================================================
    // Callback Functions
    // ========================================================

    // Example:
    //
    // void timer_callback()
    // {
    //     RCLCPP_INFO(
    //         this->get_logger(),
    //         "Timer callback executed"
    //     );
    // }


    // ========================================================
    // Node Members
    // ========================================================

    // Example:
    //
    // rclcpp::TimerBase::SharedPtr timer_;
};


// ============================================================
// Main Function
// ============================================================

int main(int argc, char * argv[])
{
    // Initialize ROS 2
    rclcpp::init(argc, argv);

    // Create the node
    auto node = std::make_shared<MyNode>();

    // Keep the node running and process callbacks
    rclcpp::spin(node);

    // Shut down ROS 2
    rclcpp::shutdown();

    return 0;
}