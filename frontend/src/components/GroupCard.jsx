const GroupCard = ({contact,idx})=> {
    return(
        <div key={idx} className="card mb-3 shadow-sm">
          <div className="card-body">
            {contact.name && <h5 className="card-title"> {contact.name || ""}</h5>}
            <p className="card-text text-truncate" style={{ maxHeight: "4.5em" }}>
              {contact['description'] || ""}
            </p>
            <div className="row small text-secondary">
              <div className="col-md-6">
                <p><strong>Company:</strong> {contact['u_company'] || "-"}</p>
                <p><strong>Manager:</strong> {contact['manager'] || "-"}</p>
                <p><strong>Location:</strong> {contact['u_location'] || "-"}</p>
                <p><strong>Group Category:</strong> {contact["u_group_category"] || "-"}</p>
              </div>
            </div>
          </div>
        </div>

    )
}
 export default GroupCard;